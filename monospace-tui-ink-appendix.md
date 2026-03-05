# Monospace Design TUI Ink Appendix

**Version: ALPHA** — Section structure and mapping notes. Not yet a complete appendix.

**Package:** `mono-tui`

This document maps the [Monospace Design TUI Standard](monospace-tui-design-standard.md) to [Ink](https://github.com/vadimdemedes/ink) (Node.js/TypeScript) with the companion library [@inkjs/ui](https://github.com/vadimdemedes/ink-ui). It assumes familiarity with the standard and the [Rendering Reference](monospace-tui-rendering-reference.md).

**Architecture:** Ink is **React for the terminal**. Standard React function components, hooks (`useState`, `useEffect`, `useRef`, `useMemo`), and JSX drive the UI. Layout uses Yoga (Facebook's Flexbox engine). Virtual DOM diffing minimizes terminal writes. Unidirectional data flow via React state management.

---

## §TI1 Component Mapping

### §TI1.1 Component Table

| Monospace TUI Component (Standard §4) | Ink Component | Package | Notes |
|----------------------------------------|--------------|---------|-------|
| Entry field | `TextInput` | `@inkjs/ui` | Placeholder, validation |
| Entry field (email) | `EmailInput` | `@inkjs/ui` | Email-specific validation |
| Entry field (password) | `PasswordInput` | `@inkjs/ui` | Masked input |
| Toggle / Confirm | `ConfirmInput` | `@inkjs/ui` | Yes/No with customizable labels |
| Select (exclusive) | `Select` | `@inkjs/ui` | Single selection from options |
| Multi-select | `MultiSelect` | `@inkjs/ui` | Multiple selection with checkboxes |
| Progress bar | `ProgressBar` | `@inkjs/ui` | Percentage fill |
| Spinner | `Spinner` | `@inkjs/ui` | Multiple styles |
| Status indicator | `StatusMessage` | `@inkjs/ui` | Success/warning/error with icon |
| Alert | `Alert` | `@inkjs/ui` | Bordered message with variant |
| Ordered list | `OrderedList` | `@inkjs/ui` | Numbered items |
| Unordered list | `UnorderedList` | `@inkjs/ui` | Bulleted items |
| Badge | `Badge` | `@inkjs/ui` | Colored label |
| Styled text | `<Text>` | `ink` | Bold, dim, italic, underline, color |
| Layout container | `<Box>` | `ink` | Flexbox layout, borders, padding |
| Spacer | `<Spacer>` | `ink` | Flex fill |
| Static output | `<Static>` | `ink` | Permanent (non-rerendering) output |

### §TI1.2 Missing Components

| Monospace TUI Component | Implementation Strategy |
|--------------------------|------------------------|
| Data table | Custom component: `<Box flexDirection="column">` with header + rows |
| Push button | Custom component: `<Box borderStyle="single"><Text>` with `useInput` |
| Radio group | Custom component or use `Select` with limited options |
| List box (scrollable) | Custom component: virtualised list with highlight bar |
| Spin button | Custom component: value display with up/down key handlers |
| Metric card | `<Box borderStyle="single" width={N}><Text bold>` |
| Sparkline | Custom component using Braille characters (§R6) |
| Tabs | Custom component: horizontal `<Box>` with active indicator |
| Tree view | Custom component: indented list with expand/collapse |
| Action bar / menus | Custom component: horizontal `<Text>` items |
| Footer key strip | Custom component (see §TI3.3) |

---

## §TI2 Layout System

### §TI2.1 Three-Region Layout via Flexbox

TODO: Map Standard §1.3 to Ink's `<Box>` Flexbox model.

```tsx
import { Box, Text } from 'ink';

function AppLayout({ children }: { children: React.ReactNode }) {
  const { columns, rows } = useStdout();

  return (
    <Box flexDirection="column" width={columns} height={rows}>
      {/* Body: A | B | C */}
      <Box flexDirection="row" flexGrow={1}>
        {/* Region A — Navigation */}
        <Box width={16} flexShrink={0} borderStyle="single" borderRight>
          <Navigation />
        </Box>

        {/* Region B — Content */}
        <Box flexGrow={1}>
          {children}
        </Box>

        {/* Region C — Context */}
        <Box width={30} flexShrink={0} borderStyle="single" borderLeft>
          <ContextPanel />
        </Box>
      </Box>

      {/* Footer key strip (§1.4) */}
      <Box height={1} flexShrink={0}>
        <FooterKeyStrip />
      </Box>
    </Box>
  );
}
```

### §TI2.2 Responsive Breakpoints

TODO: Map Standard §1.6 to conditional rendering based on terminal width.

```tsx
import { useStdout } from 'ink';

function ResponsiveLayout() {
  const { columns } = useStdout();

  const showNav = columns >= 80;
  const showContext = columns >= 120;
  const navWidth = columns >= 160 ? 20 : columns >= 120 ? 16 : 12;

  return (
    <Box flexDirection="row" flexGrow={1}>
      {showNav && <Box width={navWidth}><Navigation /></Box>}
      <Box flexGrow={1}><Content /></Box>
      {showContext && <Box width={30}><ContextPanel /></Box>}
    </Box>
  );
}
```

---

## §TI3 Keyboard Handling

### §TI3.1 Key Input via useInput

TODO: Map Standard §2.2 to Ink's `useInput` hook.

```tsx
import { useInput } from 'ink';

function App() {
  useInput((input, key) => {
    // Tier 1 — Global
    if (input === 'q' || input === 'Q') quit();
    if (key.escape) back();
    if (input === '?' || key.f1) help();
    if (input === 'r' || input === 'R' || key.f5) refresh();
    if (input === '/') filter();

    // Tier 2 — Context-dependent (route based on focus)
    // ...
  });
}
```

### §TI3.2 Focus Management

TODO: Map Standard §2.5 to Ink's `useFocus` and `useFocusManager`.

```tsx
import { useFocus, useFocusManager } from 'ink';

function InteractiveItem({ id }: { id: string }) {
  const { isFocused } = useFocus({ id });

  return (
    <Box borderStyle={isFocused ? 'double' : 'single'}>
      <Text inverse={isFocused}>Item {id}</Text>
    </Box>
  );
}
```

### §TI3.3 Footer Key Strip Component

TODO: Custom component for Standard §1.4.

```tsx
function FooterKeyStrip({ bindings }: { bindings: KeyBinding[] }) {
  return (
    <Box>
      {bindings.filter(b => b.active).map(b => (
        <Box key={b.key} marginRight={2}>
          <Text bold>{b.display}</Text>
          <Text> {b.label}</Text>
        </Box>
      ))}
    </Box>
  );
}
```

---

## §TI4 Styling and Color

### §TI4.1 Semantic Color Theme

TODO: Map Standard §5.1 to Ink's `ThemeProvider` from `@inkjs/ui`.

```tsx
import { ThemeProvider } from '@inkjs/ui';

const monoTuiTheme = {
  primary: '#5fafff',
  secondary: '#87afaf',
  tertiary: '#5fd7af',
  error: '#ff0000',
  success: '#00d700',
  warning: '#ffd700',
  surface: '#1c1c1c',
  text: '#d0d0d0',
  disabled: '#585858',
};

function App() {
  return (
    <ThemeProvider theme={monoTuiTheme}>
      <AppLayout />
    </ThemeProvider>
  );
}
```

### §TI4.2 Typography Mapping

TODO: Map Standard §7.1 to `<Text>` props.

| Treatment | `<Text>` Props |
|-----------|---------------|
| Display | `bold` + uppercase in source |
| Title | `bold` |
| Body | (default) |
| Label | `dimColor` |

### §TI4.3 State Rendering

TODO: Map Standard §8.1 to `<Text>` and `<Box>` props.

| State | Props |
|-------|-------|
| Enabled | Default |
| Focused | `inverse` or `borderStyle="double"` |
| Selected | `inverse` + marker |
| Disabled | `dimColor` |
| Error | `color="red"` |

### §TI4.4 Elevation via borderStyle

TODO: Map Standard §6.1.

| Elevation | `borderStyle` | Shadow |
|-----------|--------------|--------|
| Level 0 | None | None |
| Level 1 | `"single"` | None |
| Level 2 | `"single"` | Not supported natively |
| Level 3 | `"double"` | Not supported natively |
| Level 4 | `"double"` | Not supported natively |

Note: Ink's Flexbox renderer does not support overlapping content, making shadow rendering and scrim difficult. These would require post-processing the output buffer, which Ink does not expose.

---

## §TI5 Screen and Navigation Management

### §TI5.1 Screen State via React State

TODO: Map Standard §3.1 and §12 to React conditional rendering.

```tsx
type Screen = 'list' | 'detail' | 'edit';

function App() {
  const [screen, setScreen] = useState<Screen>('list');
  const [screenStack, setScreenStack] = useState<Screen[]>([]);

  const pushScreen = (s: Screen) => {
    setScreenStack(prev => [...prev, screen]);
    setScreen(s);
  };

  const popScreen = () => {
    setScreenStack(prev => {
      const next = [...prev];
      const last = next.pop();
      if (last) setScreen(last);
      return next;
    });
  };

  switch (screen) {
    case 'list': return <ListScreen onSelect={id => pushScreen('detail')} />;
    case 'detail': return <DetailScreen onBack={popScreen} />;
    case 'edit': return <EditScreen onBack={popScreen} />;
  }
}
```

### §TI5.2 Workflow Archetype Patterns

TODO: Mapping for each workflow archetype.

| Workflow (§12) | Ink Pattern |
|----------------|-------------|
| Wizard (§12.1) | Step state + conditional rendering; multi-step form with state accumulation |
| CRUD (§12.2) | Screen state: list/detail/edit; React state preserves list position |
| Monitor-Respond (§12.3) | `useEffect` with `setInterval` for polling; `useState` for data |
| Search-Act (§12.4) | `TextInput` + filtered list; `useState` for query and results |
| Drill-Down (§12.5) | Screen stack (push/pop); breadcrumb from stack |
| Pipeline (§12.6) | Stage state; `ProgressBar` during execution |
| Review-Approve (§12.7) | Queue index state; auto-advance via `setState` |
| Configuration (§12.8) | Tab state with per-tab form state objects |

---

## §TI6 Async Operations

### §TI6.1 useEffect for Data Fetching

TODO: Map Standard §10.2 to React patterns.

```tsx
function Dashboard() {
  const [data, setData] = useState<Data | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const interval = setInterval(async () => {
      const result = await fetchMetrics();
      setData(result);
      setLoading(false);
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  if (loading) return <Spinner label="Loading..." />;
  return <DashboardView data={data} />;
}
```

---

## §TI7 Compliance Gap Summary

| Standard Rule | Status | Notes |
|---------------|--------|-------|
| §1.3 Three-region layout | Full support | Flexbox maps naturally |
| §1.4 Footer key strip | Custom component needed | No built-in |
| §2.2 Key assignments | `useInput` hook | Manual routing required |
| §4.1 Widget selection | Partial | `@inkjs/ui` covers inputs, selects; no data table, tree |
| §5.1 Semantic colors | `ThemeProvider` | Good support via `@inkjs/ui` |
| §6.1 Elevation | Partial | Border styles yes; shadows/scrim not possible |
| §6.4 Shadow rendering | Not possible | Flexbox cannot overlap content |
| §6.5 Scrim | Not possible | No z-index or overlay support |
| §8.1 State model | React state | Standard React patterns |
| §8.2 Focus invariant | `useFocus` / `useFocusManager` | Built-in Tab cycling |
| §9.1 Accessible mode | Not built-in | No screen reader integration |
| §10.2 Long-operation feedback | `Spinner`, `ProgressBar` | Good support |
| §12 Workflow archetypes | React state patterns | All achievable via conditional rendering |

**Strengths:** React's component model and Flexbox layout make Ink the most approachable framework for developers with web experience. The `@inkjs/ui` component library covers common form widgets. Focus management is built in. State management via React hooks is well-understood.

**Weaknesses:** No overlay/z-index support makes elevation Levels 2-4 (shadows, scrim) impossible without post-processing. No built-in data table, tree, or tab components. Limited border styles compared to full Unicode box-drawing set.
